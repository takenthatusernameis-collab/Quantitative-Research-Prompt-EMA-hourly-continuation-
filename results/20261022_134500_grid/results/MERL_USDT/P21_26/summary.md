# EMA Hourly Continuation — MERL/USDT P21_26

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.3038 |
| net_win_rate | 0.3829 |
| gross_profit_factor | 0.5991 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -11.9187 |
| sortino_ratio | -5.8488 |
| max_drawdown | 0.9995 |
| cagr | -0.9505 |
| net_avg_win | 9.5237 |
| net_avg_loss | -19.4532 |
| avg_hold_time_bars | 2.0761 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
