# EMA Hourly Continuation — STRAX/USDT P12_21

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.4150 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.6530 |
| gross_win_rate | 0.4161 |
| sharpe_ratio | -5.9062 |
| sortino_ratio | -2.0247 |
| max_drawdown | 0.9059 |
| cagr | -0.6092 |
| net_avg_win | 26.9510 |
| net_avg_loss | -46.2780 |
| avg_hold_time_bars | 6.2517 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
