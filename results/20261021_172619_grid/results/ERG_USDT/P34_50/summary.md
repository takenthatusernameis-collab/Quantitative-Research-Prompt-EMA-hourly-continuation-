# EMA Hourly Continuation — ERG/USDT P34_50

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.5025 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.7202 |
| gross_win_rate | 0.4204 |
| sharpe_ratio | -3.1239 |
| sortino_ratio | -0.6684 |
| max_drawdown | 0.5361 |
| cagr | -0.2635 |
| net_avg_win | 56.9994 |
| net_avg_loss | -82.2589 |
| avg_hold_time_bars | 7.3097 |
| exposure | 0.0751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
