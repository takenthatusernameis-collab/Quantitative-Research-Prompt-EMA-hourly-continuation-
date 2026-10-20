# EMA Hourly Continuation — GLM/USDT P26_34

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.3015 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -11.4016 |
| sortino_ratio | -5.2942 |
| max_drawdown | 0.9989 |
| cagr | -0.9335 |
| net_avg_win | 10.3377 |
| net_avg_loss | -22.9899 |
| avg_hold_time_bars | 2.7228 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
