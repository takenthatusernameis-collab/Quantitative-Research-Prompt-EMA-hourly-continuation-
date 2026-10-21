# EMA Hourly Continuation — INJ/USDT P8_89

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7403 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -2.1003 |
| sortino_ratio | -0.6743 |
| max_drawdown | 0.5586 |
| cagr | -0.2674 |
| net_avg_win | 64.6822 |
| net_avg_loss | -77.0558 |
| avg_hold_time_bars | 26.5137 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
