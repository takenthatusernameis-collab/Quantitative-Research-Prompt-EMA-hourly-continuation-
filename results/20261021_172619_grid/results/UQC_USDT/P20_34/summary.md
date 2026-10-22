# EMA Hourly Continuation — UQC/USDT P20_34

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.3662 |
| net_win_rate | 0.3190 |
| gross_profit_factor | 0.6009 |
| gross_win_rate | 0.3448 |
| sharpe_ratio | -5.0218 |
| sortino_ratio | -1.0803 |
| max_drawdown | 0.7264 |
| cagr | -0.4015 |
| net_avg_win | 56.6890 |
| net_avg_loss | -72.4999 |
| avg_hold_time_bars | 42.6250 |
| exposure | 0.4476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
