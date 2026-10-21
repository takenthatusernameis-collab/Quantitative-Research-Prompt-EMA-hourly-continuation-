# EMA Hourly Continuation — WIN/USDT P26_89

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.5285 |
| gross_profit_factor | 1.1030 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -1.3788 |
| sortino_ratio | -0.3904 |
| max_drawdown | 0.4701 |
| cagr | -0.1653 |
| net_avg_win | 65.5442 |
| net_avg_loss | -93.5129 |
| avg_hold_time_bars | 17.4326 |
| exposure | 0.3059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
