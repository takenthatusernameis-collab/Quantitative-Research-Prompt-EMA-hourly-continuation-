# EMA Hourly Continuation — OGN/USDT P8_200

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.7964 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -2.1816 |
| sortino_ratio | -0.5212 |
| max_drawdown | 0.4894 |
| cagr | -0.2132 |
| net_avg_win | 69.8230 |
| net_avg_loss | -83.7835 |
| avg_hold_time_bars | 61.8258 |
| exposure | 0.8029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
