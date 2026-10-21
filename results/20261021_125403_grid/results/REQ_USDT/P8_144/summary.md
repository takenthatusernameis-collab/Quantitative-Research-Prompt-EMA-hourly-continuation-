# EMA Hourly Continuation — REQ/USDT P8_144

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.7543 |
| gross_win_rate | 0.4204 |
| sharpe_ratio | -4.6185 |
| sortino_ratio | -1.5184 |
| max_drawdown | 0.8336 |
| cagr | -0.5070 |
| net_avg_win | 48.7466 |
| net_avg_loss | -61.5415 |
| avg_hold_time_bars | 25.3130 |
| exposure | 0.6213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
