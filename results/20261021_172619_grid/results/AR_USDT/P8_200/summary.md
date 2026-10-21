# EMA Hourly Continuation — AR/USDT P8_200

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.9555 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0631 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -0.1643 |
| sortino_ratio | -0.0326 |
| max_drawdown | 0.1130 |
| cagr | -0.0179 |
| net_avg_win | 97.1885 |
| net_avg_loss | -108.3451 |
| avg_hold_time_bars | 100.1947 |
| exposure | 0.8653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
