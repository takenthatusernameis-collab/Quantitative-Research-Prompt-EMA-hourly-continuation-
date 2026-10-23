# EMA Hourly Continuation — TFUEL/USDT P26_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7859 |
| gross_win_rate | 0.4189 |
| sharpe_ratio | -6.5437 |
| sortino_ratio | -2.4208 |
| max_drawdown | 0.9495 |
| cagr | -0.6914 |
| net_avg_win | 34.5992 |
| net_avg_loss | -46.5615 |
| avg_hold_time_bars | 12.9799 |
| exposure | 0.4094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
