# EMA Hourly Continuation — AVAX/USDT P20_144

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.5793 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8969 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -4.3971 |
| sortino_ratio | -1.4144 |
| max_drawdown | 0.8311 |
| cagr | -0.4996 |
| net_avg_win | 47.2968 |
| net_avg_loss | -67.5634 |
| avg_hold_time_bars | 20.1208 |
| exposure | 0.4847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
