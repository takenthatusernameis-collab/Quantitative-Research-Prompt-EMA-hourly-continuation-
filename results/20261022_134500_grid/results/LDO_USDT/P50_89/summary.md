# EMA Hourly Continuation — LDO/USDT P50_89

**Symbol:** LDO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.4791 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.7835 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -6.1639 |
| sortino_ratio | -2.3303 |
| max_drawdown | 0.9414 |
| cagr | -0.6755 |
| net_avg_win | 27.8229 |
| net_avg_loss | -44.3747 |
| avg_hold_time_bars | 4.7939 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
