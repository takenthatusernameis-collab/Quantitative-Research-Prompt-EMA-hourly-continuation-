# EMA Hourly Continuation — QNT/USDT P12_50

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.4237 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.7997 |
| sortino_ratio | -4.3792 |
| max_drawdown | 0.9957 |
| cagr | -0.8853 |
| net_avg_win | 13.2156 |
| net_avg_loss | -24.9321 |
| avg_hold_time_bars | 5.5156 |
| exposure | 0.3126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
