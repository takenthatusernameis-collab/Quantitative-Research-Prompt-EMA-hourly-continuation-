# EMA Hourly Continuation — P2P/USDT P12_26

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1326 |
| net_profit_factor | 0.2789 |
| net_win_rate | 0.3130 |
| gross_profit_factor | 0.5246 |
| gross_win_rate | 0.3167 |
| sharpe_ratio | -13.5128 |
| sortino_ratio | -6.9259 |
| max_drawdown | 0.9998 |
| cagr | -0.9698 |
| net_avg_win | 9.3174 |
| net_avg_loss | -15.2197 |
| avg_hold_time_bars | 3.6712 |
| exposure | 0.2213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
