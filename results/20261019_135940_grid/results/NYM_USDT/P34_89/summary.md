# EMA Hourly Continuation — NYM/USDT P34_89

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.2590 |
| net_win_rate | 0.3440 |
| gross_profit_factor | 0.5959 |
| gross_win_rate | 0.3761 |
| sharpe_ratio | -9.4602 |
| sortino_ratio | -3.2880 |
| max_drawdown | 0.9882 |
| cagr | -0.8275 |
| net_avg_win | 16.9249 |
| net_avg_loss | -34.2711 |
| avg_hold_time_bars | 9.3288 |
| exposure | 0.2515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
