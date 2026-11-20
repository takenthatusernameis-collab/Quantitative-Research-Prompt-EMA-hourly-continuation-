# EMA Hourly Continuation — P2P/USDT P21_34

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.2508 |
| net_win_rate | 0.2962 |
| gross_profit_factor | 0.4629 |
| gross_win_rate | 0.2981 |
| sharpe_ratio | -12.7977 |
| sortino_ratio | -5.9010 |
| max_drawdown | 0.9994 |
| cagr | -0.9483 |
| net_avg_win | 10.7570 |
| net_avg_loss | -18.0508 |
| avg_hold_time_bars | 3.7248 |
| exposure | 0.1778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
