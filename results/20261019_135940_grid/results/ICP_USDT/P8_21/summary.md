# EMA Hourly Continuation — ICP/USDT P8_21

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1673 |
| net_profit_factor | 0.4122 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -11.9783 |
| sortino_ratio | -6.9275 |
| max_drawdown | 0.9999 |
| cagr | -0.9704 |
| net_avg_win | 9.7397 |
| net_avg_loss | -17.8501 |
| avg_hold_time_bars | 2.8296 |
| exposure | 0.2152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
