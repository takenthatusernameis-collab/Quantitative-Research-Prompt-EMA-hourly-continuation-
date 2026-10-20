# EMA Hourly Continuation — GTC/USDT P21_55

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.5183 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -6.3419 |
| sortino_ratio | -2.6816 |
| max_drawdown | 0.9606 |
| cagr | -0.7208 |
| net_avg_win | 25.9329 |
| net_avg_loss | -40.1521 |
| avg_hold_time_bars | 6.0615 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
