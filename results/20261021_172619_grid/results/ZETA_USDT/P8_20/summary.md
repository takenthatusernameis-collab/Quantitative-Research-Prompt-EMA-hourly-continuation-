# EMA Hourly Continuation — ZETA/USDT P8_20

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7865 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0950 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -2.2530 |
| sortino_ratio | -0.8240 |
| max_drawdown | 0.6672 |
| cagr | -0.3144 |
| net_avg_win | 67.7364 |
| net_avg_loss | -91.3186 |
| avg_hold_time_bars | 5.4992 |
| exposure | 0.1615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
