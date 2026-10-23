# EMA Hourly Continuation — MOG/USDT P100_200

**Symbol:** MOG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9387 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.6710 |
| sortino_ratio | -0.7586 |
| max_drawdown | 0.5914 |
| cagr | -0.3040 |
| net_avg_win | 69.1000 |
| net_avg_loss | -92.8790 |
| avg_hold_time_bars | 9.1903 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
