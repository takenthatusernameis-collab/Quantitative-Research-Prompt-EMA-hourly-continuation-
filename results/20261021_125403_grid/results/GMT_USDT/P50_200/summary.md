# EMA Hourly Continuation — GMT/USDT P50_200

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.9133 |
| net_win_rate | 0.5278 |
| gross_profit_factor | 1.1145 |
| gross_win_rate | 0.5278 |
| sharpe_ratio | -0.4385 |
| sortino_ratio | -0.1073 |
| max_drawdown | 0.1791 |
| cagr | -0.0513 |
| net_avg_win | 85.8696 |
| net_avg_loss | -105.0863 |
| avg_hold_time_bars | 30.0243 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
