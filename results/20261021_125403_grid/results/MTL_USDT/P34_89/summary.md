# EMA Hourly Continuation — MTL/USDT P34_89

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5895 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8221 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -3.6740 |
| sortino_ratio | -1.0992 |
| max_drawdown | 0.7329 |
| cagr | -0.3966 |
| net_avg_win | 52.2558 |
| net_avg_loss | -71.6345 |
| avg_hold_time_bars | 15.8352 |
| exposure | 0.3174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
