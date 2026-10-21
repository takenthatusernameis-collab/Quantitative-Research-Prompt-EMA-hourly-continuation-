# EMA Hourly Continuation — SOL/USDT P12_89

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.9730 |
| sortino_ratio | -0.6414 |
| max_drawdown | 0.5531 |
| cagr | -0.2555 |
| net_avg_win | 67.7559 |
| net_avg_loss | -86.8425 |
| avg_hold_time_bars | 20.1899 |
| exposure | 0.4735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
