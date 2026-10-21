# EMA Hourly Continuation — NOT/USDT P12_55

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.8085 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.5177 |
| sortino_ratio | -0.5372 |
| max_drawdown | 0.4958 |
| cagr | -0.2203 |
| net_avg_win | 64.2755 |
| net_avg_loss | -81.4157 |
| avg_hold_time_bars | 12.2003 |
| exposure | 0.3376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
