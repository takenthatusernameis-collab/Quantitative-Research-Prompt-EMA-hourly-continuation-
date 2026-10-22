# EMA Hourly Continuation — ONDO/USDT P50_144

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.5514 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7974 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -4.1393 |
| sortino_ratio | -1.3472 |
| max_drawdown | 0.8015 |
| cagr | -0.4681 |
| net_avg_win | 41.5909 |
| net_avg_loss | -60.0845 |
| avg_hold_time_bars | 10.5151 |
| exposure | 0.2533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
