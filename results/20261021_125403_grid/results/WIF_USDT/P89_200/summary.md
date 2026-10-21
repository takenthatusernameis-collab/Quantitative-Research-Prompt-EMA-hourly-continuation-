# EMA Hourly Continuation — WIF/USDT P89_200

**Symbol:** WIF/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7654 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.2621 |
| sortino_ratio | -0.2887 |
| max_drawdown | 0.3233 |
| cagr | -0.1246 |
| net_avg_win | 74.7125 |
| net_avg_loss | -91.0130 |
| avg_hold_time_bars | 13.6809 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
