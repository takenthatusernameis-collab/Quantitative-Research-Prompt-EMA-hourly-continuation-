# EMA Hourly Continuation — BSV/USDT P55_200

**Symbol:** BSV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7409 |
| gross_win_rate | 0.4212 |
| sharpe_ratio | -3.2126 |
| sortino_ratio | -0.8251 |
| max_drawdown | 0.6177 |
| cagr | -0.3164 |
| net_avg_win | 60.2272 |
| net_avg_loss | -76.0433 |
| avg_hold_time_bars | 24.5333 |
| exposure | 0.3680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
