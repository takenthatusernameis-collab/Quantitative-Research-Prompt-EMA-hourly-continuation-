# EMA Hourly Continuation — TFUEL/USDT P8_34

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1522 |
| net_profit_factor | 0.4538 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -11.3010 |
| sortino_ratio | -6.2067 |
| max_drawdown | 0.9996 |
| cagr | -0.9538 |
| net_avg_win | 13.3540 |
| net_avg_loss | -20.3354 |
| avg_hold_time_bars | 5.0191 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
