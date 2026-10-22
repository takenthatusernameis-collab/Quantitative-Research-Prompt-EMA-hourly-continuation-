# EMA Hourly Continuation — ARB/USDT P8_200

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.8707 |
| net_win_rate | 0.5369 |
| gross_profit_factor | 1.1258 |
| gross_win_rate | 0.5369 |
| sharpe_ratio | -0.5419 |
| sortino_ratio | -0.1093 |
| max_drawdown | 0.2730 |
| cagr | -0.0527 |
| net_avg_win | 78.6035 |
| net_avg_loss | -104.6805 |
| avg_hold_time_bars | 95.0640 |
| exposure | 0.8772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
