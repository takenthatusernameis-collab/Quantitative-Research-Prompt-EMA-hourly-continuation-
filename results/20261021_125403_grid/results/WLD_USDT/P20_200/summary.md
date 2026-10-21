# EMA Hourly Continuation — WLD/USDT P20_200

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 1.1725 |
| net_win_rate | 0.5673 |
| gross_profit_factor | 1.3027 |
| gross_win_rate | 0.5673 |
| sharpe_ratio | 0.8127 |
| sortino_ratio | 0.1862 |
| max_drawdown | 0.0797 |
| cagr | 0.0781 |
| net_avg_win | 101.6431 |
| net_avg_loss | -113.6768 |
| avg_hold_time_bars | 60.0653 |
| exposure | 0.6689 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
