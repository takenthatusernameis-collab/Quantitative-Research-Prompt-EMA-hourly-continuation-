# EMA Hourly Continuation — QNT/USDT P8_144

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -4.1647 |
| sortino_ratio | -1.5160 |
| max_drawdown | 0.8541 |
| cagr | -0.5240 |
| net_avg_win | 35.2732 |
| net_avg_loss | -56.3520 |
| avg_hold_time_bars | 21.8632 |
| exposure | 0.6758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
