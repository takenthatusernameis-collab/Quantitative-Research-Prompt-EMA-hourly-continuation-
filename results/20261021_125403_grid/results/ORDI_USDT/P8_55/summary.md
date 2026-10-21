# EMA Hourly Continuation — ORDI/USDT P8_55

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7544 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.5417 |
| sortino_ratio | -0.9495 |
| max_drawdown | 0.6789 |
| cagr | -0.3541 |
| net_avg_win | 62.5846 |
| net_avg_loss | -75.1485 |
| avg_hold_time_bars | 15.0378 |
| exposure | 0.4703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
