# EMA Hourly Continuation — ENS/USDT P20_26

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.4763 |
| sortino_ratio | -0.3066 |
| max_drawdown | 0.3237 |
| cagr | -0.1312 |
| net_avg_win | 71.2065 |
| net_avg_loss | -104.9018 |
| avg_hold_time_bars | 5.0673 |
| exposure | 0.0479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
