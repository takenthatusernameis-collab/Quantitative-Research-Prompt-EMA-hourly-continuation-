# EMA Hourly Continuation — FET/USDT P100_144

**Symbol:** FET/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.8033 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0295 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -0.9200 |
| sortino_ratio | -0.1788 |
| max_drawdown | 0.2342 |
| cagr | -0.0793 |
| net_avg_win | 82.3054 |
| net_avg_loss | -105.8752 |
| avg_hold_time_bars | 8.5082 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
