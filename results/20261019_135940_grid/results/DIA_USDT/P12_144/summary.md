# EMA Hourly Continuation — DIA/USDT P12_144

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9727 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.6941 |
| sortino_ratio | -0.8590 |
| max_drawdown | 0.6793 |
| cagr | -0.3365 |
| net_avg_win | 58.1442 |
| net_avg_loss | -79.9230 |
| avg_hold_time_bars | 27.5562 |
| exposure | 0.6434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
