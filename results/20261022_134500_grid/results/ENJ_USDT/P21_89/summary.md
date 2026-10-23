# EMA Hourly Continuation — ENJ/USDT P21_89

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.6232 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9882 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -4.6999 |
| sortino_ratio | -1.7718 |
| max_drawdown | 0.8904 |
| cagr | -0.5735 |
| net_avg_win | 43.4952 |
| net_avg_loss | -60.5927 |
| avg_hold_time_bars | 11.8451 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
