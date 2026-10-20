# EMA Hourly Continuation — ORDI/USDT P12_200

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7278 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.3497 |
| sortino_ratio | -0.6797 |
| max_drawdown | 0.5992 |
| cagr | -0.2731 |
| net_avg_win | 73.2979 |
| net_avg_loss | -92.0171 |
| avg_hold_time_bars | 37.8741 |
| exposure | 0.7248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
