# EMA Hourly Continuation — ZRX/USDT P12_55

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.5456 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -5.7314 |
| sortino_ratio | -2.5014 |
| max_drawdown | 0.9543 |
| cagr | -0.7004 |
| net_avg_win | 25.3896 |
| net_avg_loss | -40.7404 |
| avg_hold_time_bars | 9.2147 |
| exposure | 0.4038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
