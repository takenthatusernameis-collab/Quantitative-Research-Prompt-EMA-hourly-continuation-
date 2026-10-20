# EMA Hourly Continuation — GLM/USDT P26_89

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5207 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -4.9535 |
| sortino_ratio | -1.8385 |
| max_drawdown | 0.8924 |
| cagr | -0.5852 |
| net_avg_win | 30.3226 |
| net_avg_loss | -49.6677 |
| avg_hold_time_bars | 10.3954 |
| exposure | 0.3275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
