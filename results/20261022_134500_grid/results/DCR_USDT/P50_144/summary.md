# EMA Hourly Continuation — DCR/USDT P50_144

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.5070 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8130 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -4.9180 |
| sortino_ratio | -1.6191 |
| max_drawdown | 0.8609 |
| cagr | -0.5414 |
| net_avg_win | 37.0091 |
| net_avg_loss | -56.2767 |
| avg_hold_time_bars | 10.9126 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
