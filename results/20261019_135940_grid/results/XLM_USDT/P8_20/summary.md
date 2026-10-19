# EMA Hourly Continuation — XLM/USDT P8_20

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1789 |
| net_profit_factor | 0.1643 |
| net_win_rate | 0.4002 |
| gross_profit_factor | 0.7390 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -15.5175 |
| sortino_ratio | -9.3579 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 2.7454 |
| net_avg_loss | -11.1516 |
| avg_hold_time_bars | 2.6260 |
| exposure | 0.2135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
