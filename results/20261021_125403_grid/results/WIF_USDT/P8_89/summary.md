# EMA Hourly Continuation — WIF/USDT P8_89

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8041 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.5845 |
| sortino_ratio | -0.4944 |
| max_drawdown | 0.5276 |
| cagr | -0.2055 |
| net_avg_win | 77.9801 |
| net_avg_loss | -89.9684 |
| avg_hold_time_bars | 28.0896 |
| exposure | 0.6129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
