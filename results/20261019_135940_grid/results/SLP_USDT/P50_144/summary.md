# EMA Hourly Continuation — SLP/USDT P50_144

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -4.2242 |
| sortino_ratio | -1.4363 |
| max_drawdown | 0.8325 |
| cagr | -0.5001 |
| net_avg_win | 48.4111 |
| net_avg_loss | -68.5459 |
| avg_hold_time_bars | 11.5043 |
| exposure | 0.3038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
