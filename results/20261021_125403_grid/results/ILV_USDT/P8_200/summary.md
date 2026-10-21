# EMA Hourly Continuation — ILV/USDT P8_200

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 1.1065 |
| net_win_rate | 0.5688 |
| gross_profit_factor | 1.2917 |
| gross_win_rate | 0.5688 |
| sharpe_ratio | 0.5308 |
| sortino_ratio | 0.1143 |
| max_drawdown | 0.1113 |
| cagr | 0.0459 |
| net_avg_win | 100.0794 |
| net_avg_loss | -119.3171 |
| avg_hold_time_bars | 84.9817 |
| exposure | 0.8421 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
