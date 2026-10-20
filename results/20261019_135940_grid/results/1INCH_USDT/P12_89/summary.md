# EMA Hourly Continuation — 1INCH/USDT P12_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7899 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -5.6973 |
| sortino_ratio | -2.0733 |
| max_drawdown | 0.9207 |
| cagr | -0.6326 |
| net_avg_win | 33.5908 |
| net_avg_loss | -49.0803 |
| avg_hold_time_bars | 19.5381 |
| exposure | 0.5941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
