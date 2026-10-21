# EMA Hourly Continuation — XEC/USDT P34_200

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1130 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -0.7522 |
| sortino_ratio | -0.2009 |
| max_drawdown | 0.3411 |
| cagr | -0.0908 |
| net_avg_win | 82.8858 |
| net_avg_loss | -106.1561 |
| avg_hold_time_bars | 31.7341 |
| exposure | 0.4969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
