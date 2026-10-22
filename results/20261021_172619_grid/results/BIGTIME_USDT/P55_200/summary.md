# EMA Hourly Continuation — BIGTIME/USDT P55_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.8773 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0648 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -0.6866 |
| sortino_ratio | -0.1671 |
| max_drawdown | 0.2760 |
| cagr | -0.0763 |
| net_avg_win | 87.0264 |
| net_avg_loss | -105.5773 |
| avg_hold_time_bars | 29.1488 |
| exposure | 0.3812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
