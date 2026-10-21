# EMA Hourly Continuation — BONK/USDT P12_21

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0797 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.9066 |
| sortino_ratio | -0.2157 |
| max_drawdown | 0.3120 |
| cagr | -0.0956 |
| net_avg_win | 81.9669 |
| net_avg_loss | -105.8700 |
| avg_hold_time_bars | 5.4286 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
