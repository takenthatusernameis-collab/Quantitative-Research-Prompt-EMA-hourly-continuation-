# EMA Hourly Continuation — KAS/USDT P26_144

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.8726 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0734 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -0.7589 |
| sortino_ratio | -0.2147 |
| max_drawdown | 0.2698 |
| cagr | -0.0969 |
| net_avg_win | 76.5597 |
| net_avg_loss | -95.7962 |
| avg_hold_time_bars | 21.5323 |
| exposure | 0.3788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
