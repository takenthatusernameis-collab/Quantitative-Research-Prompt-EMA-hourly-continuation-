# EMA Hourly Continuation — NYM/USDT P20_55

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 800 |
| net_profit_factor | 0.2852 |
| net_win_rate | 0.3387 |
| gross_profit_factor | 0.7332 |
| gross_win_rate | 0.3925 |
| sharpe_ratio | -11.3112 |
| sortino_ratio | -4.5828 |
| max_drawdown | 0.9978 |
| cagr | -0.9120 |
| net_avg_win | 14.6877 |
| net_avg_loss | -26.3857 |
| avg_hold_time_bars | 8.0350 |
| exposure | 0.2922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
