# EMA Hourly Continuation — XAI/USDT P12_21

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1572 |
| net_profit_factor | 0.4301 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -12.7321 |
| sortino_ratio | -7.1556 |
| max_drawdown | 0.9999 |
| cagr | -0.9727 |
| net_avg_win | 12.0726 |
| net_avg_loss | -18.5261 |
| avg_hold_time_bars | 2.4281 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
