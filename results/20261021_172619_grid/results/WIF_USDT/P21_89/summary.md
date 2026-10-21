# EMA Hourly Continuation — WIF/USDT P21_89

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8805 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -0.8476 |
| sortino_ratio | -0.2596 |
| max_drawdown | 0.4002 |
| cagr | -0.1163 |
| net_avg_win | 84.4556 |
| net_avg_loss | -100.6676 |
| avg_hold_time_bars | 16.4286 |
| exposure | 0.3398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
