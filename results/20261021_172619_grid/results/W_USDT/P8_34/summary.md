# EMA Hourly Continuation — W/USDT P8_34

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.8850 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1211 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -1.1087 |
| sortino_ratio | -0.4412 |
| max_drawdown | 0.4803 |
| cagr | -0.1885 |
| net_avg_win | 78.1709 |
| net_avg_loss | -98.9038 |
| avg_hold_time_bars | 9.0368 |
| exposure | 0.3126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
