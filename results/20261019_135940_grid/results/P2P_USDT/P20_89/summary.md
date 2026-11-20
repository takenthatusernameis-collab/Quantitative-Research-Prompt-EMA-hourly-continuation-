# EMA Hourly Continuation — P2P/USDT P20_89

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4959 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.6512 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -5.1655 |
| sortino_ratio | -1.9047 |
| max_drawdown | 0.8947 |
| cagr | -0.5919 |
| net_avg_win | 31.7729 |
| net_avg_loss | -43.1817 |
| avg_hold_time_bars | 12.1439 |
| exposure | 0.3798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
